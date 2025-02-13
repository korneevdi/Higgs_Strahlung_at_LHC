import numpy
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.backends.backend_pdf import PdfPages

#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
#plt.rc('font', serif='cm')
#plt.rc('mathtext', fontset='cm')


################################################################################
def load_histo(index,inputfile):
        f=open(inputfile)
        string="{}".format(index)
        print("loading: >",string,"< from: ",inputfile)
        reading=True
        histotxt=[]
        while reading:
                tmp=f.readline()
                if ( len(tmp) == 0 ):
                        reading=False
                else:
                        line=tmp.replace("D","E")
                        nums=[float(i) for i in line.split()]
                        iobs=int(nums[0])
                        if ( iobs == index ):
                                histotxt.append(line)
        obs,bins,xbin,xval,xerr=numpy.loadtxt(histotxt,unpack=True)
        xbin=xbin[:-1]
        xval=xval[:-1]
        xerr=xerr[:-1]
        return xbin,xval,xerr,bins

################################################################################
def load_histoPWHG(index,inputfile):
        f=open(inputfile)
        string="{}".format(index)
        print("loading: >",string,"< from: ",inputfile)
        reading=True
        histotxt=[]
        while reading:
                tmp=f.readline()
                if ( len(tmp) == 0 ):
                        reading=False
                else:
                        line=tmp.replace("D","E")
                        nums=[float(i) for i in line.split()]
                        iobs=int(nums[0])
                        if ( iobs == index ):
                                histotxt.append(line)
        obs,bins,xbin,xval,xerr=numpy.loadtxt(histotxt,unpack=True)
        xbin=xbin[:-1]
        xval=xval[:-1]
        xerr=xerr[:-1]
        return xbin,xval,xerr,bins

################################################################################
#>> color list
#colMCFM=['#00CC00','#009900']
coldarkviolet=['darkviolet','darkviolet']
colseagreen=['seagreen','seagreen']
colmagenta=['#9F0162','#9F0162']
colgreen=['#009F81','#009F81']
colRed=['#FF9999','#CC0000']
colazure=['#008DF9','#008DF9']
colplum=['#FFB2FD','#FFB2FD']
colcrimson=['#A40122','#A40122']
colorange=['#FF6E3A','#FF6E3A']
colgoldenrod=['#FFC33B','#FFC33B']

colOrange=['#FFCC99','#CC6600']
colBlue=['#66B2FF','#003DF5']
colGreenish=['#99DDB9','#00AB50']
colBlack=['#4d4d4d','#000000']



#>> hatch style
hh1='/ / / / / / / / / '
hh2='\ \ \ \ \ \ \ \ \ '
hh3='X X X X X X X X X '
hh4='+ + + + + + + + + '
hh5='X X X X X X X X X '

################################################################################
#auxiliary function for text formatting
def initializetex():
#        plt.rc({"text.usetex":True, "font.family":"serif","font.serif": ["Palatino"],'font.size':10.0})
        plt.rc({"text.usetex":True})
#        plt.rc({
#                "text.usetex": True,
#                "font.family": "sans-serif",
#                "font.sans-serif": "Helvetica",
#        })
#        plt.rc({"text.usetex":True,'font.family':'serif'})
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['axes.labelsize'] = 9.0
        plt.rcParams['axes.titlesize'] = 9.0
        plt.rcParams['legend.fontsize'] = 10.0
        plt.rcParams['xtick.labelsize'] = 10.0
        plt.rcParams['ytick.labelsize'] = 10.0
        plt.rcParams['legend.fontsize'] = 10.0
        plt.rcParams['legend.handlelength'] = 2
        plt.rcParams['hatch.linewidth']=0.2
        plt.rcParams['lines.linewidth']=0.5




        
#figure size optimization
def figsize(fig_dims):

    golden_ratio  = (numpy.sqrt(5) - 1.0) / 2.0  # because it looks good
    xratio= 12.0/15.0
        
    fig_width_in  = 6.0  # figure width in inches  
    fig_height_in = fig_width_in * xratio   # figure height in inches  
    fig_dims    = [fig_width_in, fig_height_in] # fig dims as a list  
    return fig_dims


#>>> ratio, avoiding zeroes
def myratio(tab2,tab1):
    result=numpy.zeros(len(tab1))
    for i in range(len(tab1)):
        if abs(tab1[i]) > 0.0:
            result[i] = tab2[i]/tab1[i]
        else:
            result[i] = -1.0e6
    return result


#>>> ratio, avoiding zeroes
def pb2fb(tab1):
    result=numpy.zeros(len(tab1))
    for i in range(len(tab1)):
        result[i] = 1000.0 * tab1[i]
    return result




def major_formatter(x, pos):
    return f'[{x:.2f}]'

