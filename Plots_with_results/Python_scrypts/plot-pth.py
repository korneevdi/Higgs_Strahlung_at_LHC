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
pltname='pth'
output_folder = "PDF"
os.makedirs(output_folder, exist_ok=True)

#>> index
NHi=3


#>> legend
lab0 = r"$\mathrm{d}\sigma_{\mathrm{SM}}$"
lab1 = r"$\mathrm{d}\sigma_{uW}$"
lab2 = r"$\mathrm{d}\sigma_{dW}$"
lab3 = r"$\mathrm{d}\sigma_{\phi q^{(3)}}$"
lab4 = r"$\mathrm{d}\sigma_{I}$"
lab5 = r"$\mathrm{d}\sigma_{\phi ud}$"


#>> colors:
col0=colazure
col1=colmagenta
col2=colorange
col3=colplum
col4=colgoldenrod
col5=colgreen
col6=colBlack

#>> axes labels
XLABEL0=r"$$p_{\mathrm{T},H} \;\; \mathrm{[GeV]}$$"
YLABEL1=r"$$\frac{1}{\sigma_{\mathrm{NNLO}}} \,\, \frac{\mathrm{d}\sigma_{\mathrm{NNLO}}}{\mathrm{d}p_{\mathrm{T},H}} \;\; \mathrm{[1/GeV]}$$"
YLABEL2=r"$$\frac{\mathrm{NLO}}{\mathrm{LO}}$$"
YLABEL3=r"$$\frac{\mathrm{NNLO}}{\mathrm{NLO}}$$"

#>> xlimit
XMIN0=0
XMAX0=240

YMIN0=3e-5
YMAX0=0.013

YMIN1=0.8
YMAX1=1.7

YMIN2=0.9
YMAX2=1.13

my_minor_xticks=numpy.arange(0,1000,25)
my_minor_yticks1=numpy.arange(0.0,5.0,0.25)

################################################################################
output = os.path.join(output_folder, pltname + ".pdf")

#>> load data

# Path to the data folder
data_dir = os.path.join(os.path.dirname(__file__), '../data')

### SM
xx,val_SM_LO,err_SM_LO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_SM_LO_xMuR_1.00_xMuF_1.00_ptH.histo'))
xx,val_SM_NLO,err_SM_NLO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_SM_NLO_xMuR_1.00_xMuF_1.00_ptH.histo'))
xx,val_SM_NNLO,err_SM_NNLO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_SM_NNLO_xMuR_1.00_xMuF_1.00_ptH.histo'))

### cuWsq
xx,val_cuWsq_LO,err0_cuWsq_LO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cuW_1.0_noSM_LO_xMuR_1.00_xMuF_1.00_ptH.histo'))
xx,val_cuWsq_NLO,err0_cuWsq_NLO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cuW_1.0_noSM_NLO_xMuR_1.00_xMuF_1.00_ptH.histo'))
xx,val_cuWsq_NNLO,err0_cuWsq_NNLO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cuW_1.0_noSM_NNLO_xMuR_1.00_xMuF_1.00_ptH.histo'))

### cdWsq
xx,val_cdWsq_LO,err0_cdWsq_LO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cdW_1.0_noSM_LO_xMuR_1.00_xMuF_1.00_ptH.histo'))
xx,val_cdWsq_NLO,err0_cdWsq_NLO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cdW_1.0_noSM_NLO_xMuR_1.00_xMuF_1.00_ptH.histo'))
xx,val_cdWsq_NNLO,err0_cdWsq_NNLO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cdW_1.0_noSM_NNLO_xMuR_1.00_xMuF_1.00_ptH.histo'))

### cHq3^2
xx,val_cHq3sq_LO,err0_cHq3sq_LO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cHq3_1.0_noSM_LO_xMuR_1.00_xMuF_1.00_ptH.histo'))
xx,val_cHq3sq_NLO,err0_cHq3sq_NLO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cHq3_1.0_noSM_NLO_xMuR_1.00_xMuF_1.00_ptH.histo'))
xx,val_cHq3sq_NNLO,err0_cHq3sq_NNLO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cHq3_1.0_noSM_NNLO_xMuR_1.00_xMuF_1.00_ptH.histo'))

### cHq3
xx,val_cHq3_LO,err0_cHq3_LO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cHq3Intf_LO_xMuR_1.00_xMuF_1.00_ptH.histo'))
xx,val_cHq3_NLO,err0_cHq3_NLO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cHq3Intf_NLO_xMuR_1.00_xMuF_1.00_ptH.histo'))
xx,val_cHq3_NNLO,err0_cHq3_NNLO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cHq3Intf_NNLO_xMuR_1.00_xMuF_1.00_ptH.histo'))

### cHud^2
xx,val_cHudsq_LO,err0_cHudsq_LO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cHud_1.0_noSM_LO_xMuR_1.00_xMuF_1.00_ptH.histo'))
xx,val_cHudsq_NLO,err0_cHudsq_NLO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cHud_1.0_noSM_NLO_xMuR_1.00_xMuF_1.00_ptH.histo'))
xx,val_cHudsq_NNLO,err0_cHudsq_NNLO,bins=load_histo(NHi, os.path.join(data_dir, './WpH_Hundk_fid_cHud_1.0_noSM_NNLO_xMuR_1.00_xMuF_1.00_ptH.histo'))


## normalize all NNLO results to 1

xsecSM=58.60
xseccuWsq=83.17
xseccdWsq=55.17
xseccHq3sq=70.15
xseccHq3=106.80
xseccHudsq=19.20

val_SM_NNLO_resc = val_SM_NNLO/xsecSM
val_cuWsq_NNLO_resc=val_cuWsq_NNLO/xseccuWsq
val_cdWsq_NNLO_resc=val_cdWsq_NNLO/xseccdWsq
val_cHq3sq_NNLO_resc=val_cHq3sq_NNLO/xseccHq3sq
val_cHq3_NNLO_resc=val_cHq3_NNLO/xseccHq3
val_cHudsq_NNLO_resc=val_cHudsq_NNLO/xseccHudsq

binsize=(xx[2]-xx[1]) ###(bins[1]-bins[0])
print(binsize)
val_SM_NNLO_resc=val_SM_NNLO_resc/binsize
val_cuWsq_NNLO_resc=val_cuWsq_NNLO_resc/binsize
val_cdWsq_NNLO_resc=val_cdWsq_NNLO_resc/binsize
val_cHq3sq_NNLO_resc=val_cHq3sq_NNLO_resc/binsize
val_cHq3_NNLO_resc=val_cHq3_NNLO_resc/binsize
val_cHudsq_NNLO_resc=val_cHudsq_NNLO_resc/binsize

################################################################################
fig_dims=[]
fig_dims=figsize(fig_dims)
fig = plt.figure(figsize=fig_dims)

pdf_pages = PdfPages(output)

################################################################################
#>> panels
gs = fig.add_gridspec(3, hspace=0,height_ratios=[3,1,1])
axs = gs.subplots(sharex=True, sharey=False)
ax1=axs[0]
ax2=axs[1]
ax3=axs[2]


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

ax3.set_ylabel(YLABEL3, fontsize=14)
ax3.set_xticks(my_minor_xticks,minor=True)
ax3.set_yticks(my_minor_yticks1,minor=True)
ax3.grid(dashes=[10,10],linewidth=0.1,which='both')
ax3.tick_params(direction='in')


#>> plot things (panel [1],linewidth=1.0)
p0a,= ax1.step(xx,val_SM_NNLO_resc,where='post',color=col0[1],linewidth=1.0)
p1a,= ax1.step(xx,val_cuWsq_NNLO_resc,where='post',color=col1[1],linewidth=1.0)
p2a,= ax1.step(xx,val_cdWsq_NNLO_resc,where='post',color=col2[1],linewidth=1.0)
p3a,= ax1.step(xx,val_cHq3sq_NNLO_resc,where='post',color=col3[1],linewidth=1.0)
p4a,= ax1.step(xx,val_cHq3_NNLO_resc,where='post',color=col4[1],linewidth=1.0)
p5a,= ax1.step(xx,val_cHudsq_NNLO_resc,where='post',color=col5[1],linewidth=1.0)

p0b,= [plt.Rectangle((0,0),0,0,facecolor='none',linewidth=0.2,edgecolor=col0[0],alpha=None)]
p1b,= [plt.Rectangle((0,0),0,0,facecolor='none',linewidth=0.2,edgecolor=col1[0],alpha=None)]
p2b,= [plt.Rectangle((0,0),0,0,facecolor='none',linewidth=0.2,edgecolor=col2[0],alpha=None)]
p3b,= [plt.Rectangle((0,0),0,0,facecolor='none',linewidth=0.2,edgecolor=col3[0],alpha=None)]
p4b,= [plt.Rectangle((0,0),0,0,facecolor='none',linewidth=0.2,edgecolor=col4[0],alpha=None)]
p5b,= [plt.Rectangle((0,0),0,0,facecolor='none',linewidth=0.2,edgecolor=col5[0],alpha=None)]
lines1 = ((p0a,p0b),(p1a,p1b),(p2a,p2b))
lines2 = ((p3a,p3b),(p4a,p4b),(p5a,p5b))
legend1=(lab0,lab1,lab2)
legend2=(lab3,lab4,lab5)

ax1.set_xlim(xmin=XMIN0, xmax=XMAX0)
ax1.set_ylim(ymin=YMIN0, ymax=YMAX0)

#>> plot things (panel 2)
ax2.step(xx, myratio(val_SM_NLO,val_SM_LO), where='post',color=col0[1],linewidth=1.0)
ax2.step(xx, myratio(val_cuWsq_NLO,val_cuWsq_LO), where='post',color=col1[1],linewidth=1.0)
ax2.step(xx, myratio(val_cdWsq_NLO,val_cdWsq_LO), where='post',color=col2[1],linewidth=1.0)
ax2.step(xx, myratio(val_cHq3sq_NLO,val_cHq3sq_LO), where='post',color=col3[1],linewidth=1.0)
ax2.step(xx, myratio(val_cHq3_NLO,val_cHq3_LO), where='post',color=col4[1],linewidth=1.0)
ax2.step(xx, myratio(val_cHudsq_NLO,val_cHudsq_LO), where='post',color=col5[1],linewidth=1.0)
ax2.step(xx, myratio(val_cHudsq_NLO,val_cHudsq_NLO), where='post',color=col6[1],linewidth=1.0,linestyle='dashed')  # this is just to plot 1
ax2.set_xlim(xmin=XMIN0, xmax=XMAX0)
ax2.set_ylim(ymin=YMIN1, ymax=YMAX1)


#>> plot things (panel 2)
ax3.step(xx, myratio(val_SM_NNLO,val_SM_NLO), where='post',color=col0[1],linewidth=1.0)
ax3.step(xx, myratio(val_cuWsq_NNLO,val_cuWsq_NLO), where='post',color=col1[1],linewidth=1.0)
ax3.step(xx, myratio(val_cdWsq_NNLO,val_cdWsq_NLO), where='post',color=col2[1],linewidth=1.0)
ax3.step(xx, myratio(val_cHq3sq_NNLO,val_cHq3sq_NLO), where='post',color=col3[1],linewidth=1.0)
ax3.step(xx, myratio(val_cHq3_NNLO,val_cHq3_NLO), where='post',color=col4[1],linewidth=1.0)
ax3.step(xx, myratio(val_cHudsq_NNLO,val_cHudsq_NLO), where='post',color=col5[1],linewidth=1.0)
ax3.step(xx, myratio(val_cHudsq_NNLO,val_cHudsq_NNLO), where='post',color=col6[1],linewidth=1.0,linestyle='dashed')  # this is just to plot 1
ax3.set_xlim(xmin=XMIN0, xmax=XMAX0)
ax3.set_ylim(ymin=YMIN2, ymax=YMAX2)

#>> xlabel
plt.xlabel(XLABEL0, fontsize=16)

#>> legend
leg1=ax1.legend(lines1,legend1,loc='upper center', bbox_to_anchor=(0.6, 1.0), fontsize=12)
leg2=ax1.legend(lines2,legend2,loc='upper right', bbox_to_anchor=(1.0, 1.0), fontsize=12)
rect = leg1.get_frame()
rect.set_linewidth(0.0)
ax1.add_artist(leg1)

rect = leg2.get_frame()
rect.set_linewidth(0.0)


ax1.add_artist(leg2)


##>> legend

################################################################################
#>> put any labels in here
ax1.annotate(r'LHC 13 TeV, NNLO QCD', xy=(0.08,0.9), xycoords="axes fraction", color="#ff0000")

################################################################################
#>> save figure
pdf_pages.savefig(fig,bbox_inches='tight')
pdf_pages.close()
