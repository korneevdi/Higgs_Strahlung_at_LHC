from plotter_settings import *
import os
import matplotlib.pyplot as plt

################################################################################
initializetex()

################################################################################

# Connecting LaTeX rendering
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "text.latex.preamble": r"\usepackage{amsmath}"
})

#>> output file
pltname='mvh_comp'
output_folder = "PDF"
os.makedirs(output_folder, exist_ok=True)

#>> index
NHi=2


#>> legend
lab0=r"point $a$"
lab1=r"fit"

#>> colors:
col0=colazure
col1=colmagenta
col2=colorange
col3=colplum
col4=colgoldenrod
col5=colgreen
col6=colBlack

#>> axes labels
XLABEL0=r"$$m_{WH} \;\; \mathrm{[GeV]}$$"
YLABEL1=r"$$\frac{\mathrm{d}\sigma^{\mathrm{SMEFT}}_{\mathrm{NNLO}}}{\mathrm{d}m_{WH}} \;\; \mathrm{[fb/GeV]}$$"
YLABEL2=r"ratio"
#>> xlimit
XMIN0=200
XMAX0=600

YMIN0=-0.3
YMAX0=0.3

YMIN1=0.97
YMAX1=1.03


my_minor_xticks=numpy.arange(0,1000,25)
my_minor_yticks1=numpy.arange(0.0,5.0,0.25)

################################################################################
output = os.path.join(output_folder, pltname + ".pdf")

#>> load data

# Path to the data folder
data_dir = os.path.join(os.path.dirname(__file__), '../data')

### SM
xx,val_fit,err_fit,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_fit_cuW_0.321_cdW_0.521_cHq3_-0.718_cHud_0.451_NNLO_xMuR_1.00_xMuF_1.00_mVH.histo'))
xx,val_full,err_full,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_test2mSM_NNLO_xMuR_1.00_xMuF_1.00_mVH.histo'))


binsize=(xx[2]-xx[1]) ###(bins[1]-bins[0])
val_fit = val_fit/binsize
val_full=val_full/binsize


################################################################################
fig_dims=[]
fig_dims=figsize(fig_dims)
fig = plt.figure(figsize=fig_dims)

pdf_pages = PdfPages(output)

################################################################################
#>> panels
gs = fig.add_gridspec(2, hspace=0,height_ratios=[2,1])
axs = gs.subplots(sharex=True, sharey=False)
ax1=axs[0]
ax2=axs[1]


#>> some settings
plt.setp(ax1.get_xticklabels(),visible=False)
plt.setp(ax2.get_xticklabels(),visible=True)

ax1.set_ylabel(YLABEL1, fontsize=14)
ax1.set_xticks(my_minor_xticks,minor=True)
ax1.grid(dashes=[10,10],linewidth=0.1,which='both')
ax1.tick_params(direction='in')

ax2.set_ylabel(YLABEL2, fontsize=14)
ax2.set_xticks(my_minor_xticks,minor=True)
ax2.set_yticks(my_minor_yticks1,minor=True)
ax2.grid(dashes=[10,10],linewidth=0.1,which='both')
ax2.tick_params(direction='in')


#>> plot things (panel [1],linewidth=1.0)
p0a,= ax1.step(xx,val_fit,where='post',color=col0[1],linewidth=1.0)
p1a,= ax1.step(xx,val_full,where='post',color=col1[1],linewidth=1.0)


p0b,= [plt.Rectangle((0,0),0,0,facecolor='none',linewidth=0.2,edgecolor=col0[0],alpha=None)]
p1b,= [plt.Rectangle((0,0),0,0,facecolor='none',linewidth=0.2,edgecolor=col1[0],alpha=None)]
lines = ((p0a,p0b),(p1a,p1b))
legend=(lab0,lab1)

ax1.set_xlim(xmin=XMIN0, xmax=XMAX0)
ax1.set_ylim(ymin=YMIN0, ymax=YMAX0)

#>> plot things (panel 2)
ax2.step(xx, myratio(val_full,val_fit), where='post',color=col0[1],linewidth=1.0)

ax2.set_xlim(xmin=XMIN0, xmax=XMAX0)
ax2.set_ylim(ymin=YMIN1, ymax=YMAX1)

#>> xlabel
plt.xlabel(XLABEL0, fontsize=16)

#>> legend
leg=ax1.legend(lines,legend,loc='upper right', fontsize=12)
##
rect = leg.get_frame()
rect.set_linewidth(0.0)

################################################################################
#>> put any labels in here
ax1.annotate(r'LHC 13 TeV, NNLO QCD', xy=(0.330,0.9), xycoords="axes fraction", color="#ff0000")

################################################################################
#>> save figure
pdf_pages.savefig(fig,bbox_inches='tight')
pdf_pages.close()
