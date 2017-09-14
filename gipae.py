'''
#to be done

Try to come up with an EOF char and include it, doing which you would be able to mark the end of line and file
10 is used for EOL
then merge the multiple lists into one, convert to a square and append zeroes 
write to image

Decode in the similar way, taking the steps backwards
'''


from math import *
from numpy import *
from PIL import Image
import sys
import re




def comp_square(num):
    '''This method completes the squares of the list given, returns l,m,zero
    input: list - list of numbers to be converted into a matrix
    output: int - l: The number of rows the matrix should have
            int - m: The number of columns the matrix should have
            int - zero: The number of zeros to be added to the list in order to reshape it to a matrix
    '''
    #transforming the array into a square matrix and adding the extra number of zeros to complete the square
    l=sqrt(len(num))
    l=int(l)
    m=l+1
    elem=l*m
    zero=elem-len(num)
    if zero>=0:
        m=l+1
    else:
        l=l+1

    elem=l*m
    zero=elem-len(num)

    #print elem
    #print zero
    return l,m,zero


def encode_wrapper(fl,mx,zero):
    '''This function returns the file name and path separately for further processing
       This function also returns the path and filename where the output after decoding should be stored
    input: string - fl: The path to file with the filename
           float - mx: The maximum of the float values encoded in the image
           int - zero: The number of zeros added for completing the matrix
    output: string - fname: The name of the file separate from the path
            string - path: The path of the file, after removing the filename from it
            string - store: The path and file name where the output should be stored
    '''
    b=fl.split('/')
    fname=b[-1]
    path='/'.join(b[:-1])


    b=fname.split('.')
    fn='_'.join(b)
    if path:
        store=path+'/'+fn+'_'+str(mx)+'_'+str(zero)+'.tiff'
    else:
        store=fn+'_'+str(mx)+'_'+str(zero)+'.tiff'
        
    return fname,path,store



def encoder(num,l,m,zero,mx,precision=1):
    '''
    This is the low precision encoder
    This method encdes the floating point values as is in the image, which as a result loose precision and are accurate only upto 6 or 7 decimal places

    input: list - num: The list containing the floating point values
           int - l: The number of rows of the matrix
           int - m: The number of columns of matrix
           int - zero: The number of zeros to be appended to the matrix for completing the square
    output: numpy.ndarray - num: The input list num reshaped into a matrix form
    '''

    #append the number of zeros in 'zero' variable to num
    num.extend([0]*zero)


    if precision:
        mx=float(mx)
        num=[num[i]/float(mx) for i in range(2,len(num))]
        #inserting the precision bit and delimiter bit again as num leaves out the first two bits when dividing  
        num.insert(0,precision)
        num.insert(1,ord(delim)/255.0)

           
    #reshaping the list to form a matrix
    num=reshape(num,(l,m))

    #reducing the decimal precision
    #num=around(num, decimals=8)
    return num


def print_help():
    start = "\033[1m"
    end = "\033[0;0m"

    try:
        f=open('gipa_man.txt')
        #p=f.readlines()
        p=f.read()
        f.close()
    except:
        p="Documentation not found!"

    p=p.split('<b>')
    p=start.join(p)
    p=p.split('</b>')
    p=end.join(p)
    print p
    
    
    
def arg_parser(argv):
    '''
    This is an argument parser for the command line arguments, which can be used to interpret the delimiter and precision
    '''
    #if the first argument is help, display help, else
    #if no argument, use defaults, delim=' ', precision=1
    if len(argv)==2:
        if re.match("^--h|^-h",argv[1]):
            print_help()
            exit(0)
        else:
            delim=' '
            precision=1
            return delim,precision

        
    #if only 1 argument is specified
    if len(argv)==3:
        #if the 3rd argument is delimiter 
        if re.match("^--d|^-d",argv[2]):
            #a=argv[2].split('=')[1]
            #delim=a.split("'")[1]
            delim=argv[2].split('=')[1]
            #use default precision=1
            precision=1
            return delim,precision
        #if the 3rd argument is precision
        elif re.match("^--p|^-p",argv[2]):
            a=argv[2].split('=')[1]
            high=['high',1]
            low=['low',0]
            try:
                e=int(a)
            except:
                a=a.replace('"','')
                e=a.replace("'",'')
                #e=a.split("'")[1]
            if e in high:
                precision=1
            elif e in low:
                    precision=0
            else:
                print "Precision not recognized!"
                exit(0)
            #use default delimiter ' '
            delim=' '
            return delim,precision
        else:
            print_help()
            exit(0)
        return delim,precision

    
    #if both the arguments are present
    if len(argv)==4:
        #if 3rd arg is delimiter and 4th precision
        if re.match("^--d|^-d",argv[2]):
            #a=argv[2].split('=')[1]
            #delim=a.split("'")[1]
            delim=argv[2].split('=')[1]

            #if the 4th argument is precision 
            if re.match("^--p|^-p",argv[3]):
                a=argv[3].split('=')[1]
                high=['high',1]
                low=['low',0]
                try:
                    e=int(a)
                except:
                    a=a.replace('"','')
                    e=a.replace("'",'')
                    #e=a.split("'")[1]
                if e in high:
                    precision=1
                elif e in low:
                    precision=0
                else:
                    print "Precision not recognized!"
                    print_help()
                    exit(0)
            return delim,precision

        #if 3rd arg is precision and 4th delimiter
        elif re.match("^--p|^-p",argv[2]):
            a=argv[2].split('=')[1]
            high=['high',1]
            low=['low',0]
            try:
                e=int(a)
            except:
                a=a.replace('"','')
                e=a.replace("'",'')
                #e=a.split("'")[1]
            if e in high:
                precision=1
            elif e in low:
                    precision=0
            else:
                print "Precision not recognized!"
                exit(0)

            #if the 4th argument is delimiter
            if re.match("^--d|^-d",argv[3]):
                #a=argv[3].split('=')[1]
                #delim=a.split("'")[1]
                delim=argv[3].split('=')[1]

            return delim,precision
        else:
            print "Arguments not recognized"
            print_help()
            exit(0)

    if len(argv)>4:
        print "Number of arguments greater than expected"
        print_help()
        exit(0)

            



if __name__ == '__main__':
    if len(sys.argv) < 2: 
        print "Usage: python <name> <filename> <delimiter*> <precision*>"
        print_help()
        exit(0)

    #delim=' '
    #precision=1
    delim,precision=arg_parser(sys.argv)

    fl=sys.argv[1]
    print "Encoding "+fl
    #Enter the file name with path to be opened here
    #fl='/Users/gmalik9/Desktop/Genome Designer/Data Compresion/input-copy-2.txt'


    try:
        f=open(fl)
        #p=f.readlines()
        p=f.readlines()
        f.close()
    except:
        print("No such file or directory")
        print_help()
        exit(0)


    #merging the array into a single one read from multiple lines in the file 
    p=delim.join(p)


    #splitting the merged array based on the delimiter and converting into float
    num=p.split(delim)
    num=[float(num[i]) for i in range(0,len(num))]

    mx=max(num)

    #add precision bit and ASCII of delimiter/255.0 in the first two pixels of the image respectively
    num.insert(0,precision)
    num.insert(1,ord(delim)/255.0)

    #completing the square
    l,m,zero=comp_square(num)

    #Return the filename, path and the path+filename for the image to be stored 
    fname,path,store=encode_wrapper(fl,mx,zero)


    num=encoder(num,l,m,zero,mx,precision)

    #save it to the path from where it was taken and store it with the new name accordingly



    #try writing it to an image file now

    img1=Image.fromarray(num.astype('float'))
    #img1 = Image.fromarray(num)

    #img1.save('test.tiff')
    img1.save(store)
    print "Encoding Complete. File stored as "+store


    #remove everything under this before deployment
    #
    #
    #       |||||
    #   |||
    #   |||
    #   |||
    #   |||         omment this
    #   |||
    #   |||
    #       |||||
    #
    #
    savetxt('test.txt',num)
    #f1 is basically the equivalent of num, it is exactly num, just not in a matrix form
    #remove f1 before deployment, here only for testing
    f1 = list(img1.getdata())


