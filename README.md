# mergepdfs

Python command line program to merge multiple pdfs to one pdf.

## Usage:

```
mergepdfs [inputfiles] outputfile
```

where inputfiles either is a sequence of pdf files or the wild card symbol ´*´ which will take all pdf files in the folder.
The outputfile is the complete name of the new pdf file.

## Example:

```
mergepdfs file1.pdf file2.pdf outputfile.pdf
```

```
mergepdfs * outputfile.pdf
```

## Developer information:
For information on how to build a library like this, check out: https://github.com/HermitOS/hermitos.github.io/blob/master/CreateAPythonLibrary.md
