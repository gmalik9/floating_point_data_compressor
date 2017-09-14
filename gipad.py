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




def decode_wrapper(fl):
    '''This function returns the file name, path, maximum in the encoded image and the number of zeros added for completing the square separately for further processing
        This function also returns the path and filename where the output after decoding should be stored
    input: string - The path to file with the filename
    output: string - fname: The name of the file separate from the path
            string - path: The path of the file, after removing the filename from it
            float - mx: The maximum of the float values encoded in the image
            int - zero: The number of zeros added for completing the matrix
            string - store: The path and file name where the output should be stored
    '''
    b=fl.split('/')
    fname=b[-1]
    path='/'.join(b[:-1])

    b=fname.split('_')
    fn='.'.join(['_'.join(b[0:-3]),b[-3]])

    if path:
        store=path+'/'+fn
    else:
        store=fn


    try:
        mx=float(b[-2])
    except:
        print "Max Missing"

    zero=int(b[-1].split('.')[0])
    
    return fname,path,mx,zero,store


def decoder(f2,mx,zero):
    #removing the number of zeroes from the array/matrix, added to complete the square  
    f2=f2[:-zero]

    precision=int(f2[0])

    if precision not in [0,1]:
        print "Precision bit missing/corrupted"
        exit(0)
        
    delim=chr(int(f2[1]*255.0))

    #removing the first two bits for precision and delimiter, f2 then would hold only data
    f2=f2[2:]

    if precision:
        f2=[f2[i]*mx for i in range(0,len(f2))]

    return precision,delim,f2
        
    




#decoding begins


if __name__ == '__main__':
    if len(sys.argv) < 2: 
        print "Usage: python <name> <image>"
        exit(0)
        
    fl=sys.argv[1]
    #Enter the path of the gipa file to be decoded
    #fl='/Users/gmalik9/Desktop/Genome Designer/Data Compresion/input-copy-2_txt_4465.0_5.tiff'
    fname,path,mx,zero,store=decode_wrapper(fl)


    #read the image and store the data from it to a list
    #f2 is also the equal to num
    try:
        img2 = Image.open(fl)
    except:
        print("No such file or directory")
        exit(0)

    print "Decoding "+fl
    
    f2 = list(img2.getdata())
    #print f1 == f2


    precision,delim,f2=decoder(f2,mx,zero)

    if precision==1:
        if not isinstance(mx,float):
            print "Max not float in high precision"
            exit(0)


    ff=open(store,'w')
    ff.writelines(delim.join([str(f2[i]) for i in range(0,len(f2))]))
    ff.close()

    print "Decoding Complete. File stored as "+store


