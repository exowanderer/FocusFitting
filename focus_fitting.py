import pandas as pd
from astropy import modeling
from pylab import concatenate, plot, xlim, median, diff, axvline, ion

ion()

fit_lvmq = modeling.fitting.LevMarLSQFitter()

focusdata = pd.read_csv('focus_test_m51.data')

xvar    = focusdata['Focus_Level']
yvar1   = focusdata['Star_1']
yvar2   = focusdata['Star_2']

quadmodel = modeling.models.Polynomial1D(degree=2)

quadmodel_star1_0 = fit_lvmq(quadmodel, xvar, yvar1)
quadmodel_star1_1 = fit_lvmq(quadmodel_star1_0, xvar, yvar1)

quadmodel_star2_0 = fit_lvmq(quadmodel, xvar, yvar2)
quadmodel_star2_1 = fit_lvmq(quadmodel_star2_0, xvar, yvar2)
quadmodel_starboth_0 = fit_lvmq(quadmodel, concatenate([xvar,xvar]), concatenate([yvar1, yvar2]))
quadmodel_starboth_1 = fit_lvmq(quadmodel_starboth_0, concatenate([xvar,xvar]), concatenate([yvar1, yvar2]))

p1 = quadmodel_star1_1.parameters
p2 = quadmodel_star2_1.parameters
pB = quadmodel_starboth_1.parameters

plot(xvar, yvar1, 'o')
plot(xvar, yvar2, 'o')
plot(xvar, p1[0]+ p1[1]*xvar + p1[2]*xvar**2., 'b--', lw=2)
plot(xvar, p2[0]+ p2[1]*xvar + p2[2]*xvar**2., 'g--', lw=2)
plot(xvar, pB[0]+ pB[1]*xvar + pB[2]*xvar**2., 'r--')
dxvar   = median(diff(xvar))
xlim(xvar.min() - 0.5*dxvar, xvar.max() + 0.5*dxvar)

a1 = p1[2]
b1 = p1[1]
a2 = p2[2]
b2 = p2[1]
aB = pB[2]
bB = pB[1]
v1 = -b1 / (2*a1)
v2 = -b2 / (2*a2)
vB = -bB / (2*aB)

axvline(v1, linestyle='--', linewidth=0.5, color='b')
axvline(v2, linestyle='--', linewidth=0.5, color='g')
axvline(vB, linestyle='--', linewidth=0.5, color='r')

def quadfit_focus(xvar, yvars):
    if len(yvars) == yvars.size:
        yvars = array([yvars])
    else:
        yvars = array(yvars)

    for k in range(len(yvars)):
        plot(xvar, yvars[k], 'o', color=rcParams['axes.color_cycle'][k])
    else:
        print 'Dont Plot Data'

    quadmodel = modeling.models.Polynomial1D(degree=2)

    # for k in range(len(yvars)):
        
