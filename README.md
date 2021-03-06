# GIPA - floating_point_data_compressor
GIPA                                                                      

NAME

     gipa -- compression/decompression tool to package compress and encode massive archive files with floating-point data
USAGE

     python gipae.py [file] [-dh] [{-p}] 
    
DESCRIPTION

     The gipa program compresses and decompresses files holding
     massive amounts of floating point data.  
     The specification of all the parameters is optional. If no 
     parameter is specified, it will exit normally with the display of this man/help page. 
     If only the file is specified and no other arguments, it will
     use default arguments for precision and delimiter. 
     When compressing the input file, it will generate another 
     output file with extension '.tiff'. The output file can be 
     opened with any standard image viewer. The naming convention
     is important and should not be manipulated/modified for the 
     file to decompress properly using the counterpart of this program. 
     The naming convention followed is: name of the file being compressed_file extension_max data value_number of zeros.tiff (For more information please read the patent application). 
     
     The dependance on the naming convention is because of no additional 
     bits to the data for storing the file and then using those bits for decompression. 
     This saves some additional space without the manipulation of data. 
     There are only two bits added to the data used for the purpose of decompression. 
     The first bit is the precision mode, which is an integer in the range [0,1], 
     where 0 signifies low precision and 1 signifies high precision. In case of 
     low precision, the data is stored exactly as given in floating point into 
     the output image whereas in case of high precision, the data is scaled 
     down into another range of {0,1} and then stored in the output image. 

     Both the techniques do not manipulate the data but it is not 
     guaranteed because if the floating point numbers are not in the
     representable range or fall in the number system gaps, it may scale
     to the nearest representable number. The low precision works well 
     with around 5 to 7 decimal places whereas the high precision can 
     go even upto 22 decimal places.


     This version of gipa code is not capable of decompressing files 
     compressed using gipae. For decompressing the files, another utility
     exists called gipad. They have been separated for security purposes, 
     but can be combined to work together or could be invoked from a single shell script.

     The code is written in 
     Python 2.7.3 [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin, 
     but should work on all the distributions of python. The code is 
     dependent on two additional python libraries: PIL and numpy.
     To install:
            Numpy: pip install numpy
            or visit https://pypi.python.org/pypi/numpy for other options

            PIL: pip install pillow or pip install PIL
            or visit https://pypi.python.org/pypi/PIL for other options
            
     GIPA is also analogus to a non-neural network based auto-encoder, 
     which can be used to compress massive floating point data and the 
     representation can later be learnt using a neural network 
     or other machine learning algorithms.

OPTIONS

     The following options are available:

     
     -d, --d, -delimiter, --delimiter 
                       This option specifies the delimiter used in the 
                       file to separate the floating-point data. The file 
                       can have data separated by any delimiter except single
                       quote(') and double quote(") as they have been reserved
                       for internal purposes. The delimiter can be specified
                       on the command line in single or double quotes. 
                       This parameter is optional. 
                       Default: ' ' (space). Usage: --d=' '

     -p, --p, -precision, --precision
                       This option selects the precision mode to be used 
                       when compressing the floating-point input file. 
                       Currently only two modes are supported, high and low. 
                       High can be specified with the keyword 'high' or the integer 1, 
                       while low can be specified using 'low' or 0. 
                       If a parameter outside these 4 is specified, 
                       the program exits with a Precision not recognised error. 
                       This parameter is optional. 
                       Default: high. Usage: --p=1 or --p='high'.

     -h, --h, -help, --help        
                       This option prints this usage summary/man page and exits.

ENVIRONMENT

     The environment variable python needs to be set first 
     in order to run it from command line with arguments. 
     Options on the command line will override the options in the environment.

HISTORY

     The gipa program was originally started for the compression 
     of pointer files generated by the mapping of data of data onto
     an organism's DNA by a software called Nibble 
     (Malik and Dhar, 2015 PCT/IB2015/057964) by Girik Malik and Pawan K. Dhar. 
     The algorithm used in GIPA is called pkd.

     It was earlier written for a general compression but was later
     converted to the one for Massive Data (the word BIG DATA is not used
     here as the data is unstructured but only to a certain extent, 
     otherwise it could have been called a BIG Data Compression Tool).
AUTHORS

     This implementation of gipa was written by 
     Girik Malik <girikmalik@gmail.com>.

BUGS

     (Warning) The data may get manipulated in the trailing decimal places
     to some extent only if it is not in a representable format.

GIPA                             May 30, 2016                            
