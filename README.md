# vrml2csv
Parsing coordinates and vertex normals from a vrml file

## Usage
```
$ python ./vrml2csv.py 
Please enter the root of your vrml file:/Users/usrname/dir/root-of-your-vrml        
Converting /Users/usrname/dir/root-of-your-vrml.wrl...
Reading vertex coordinates.
Reading normal vectors.
Reading coordinate indices.
...
```

```
$ python
>>> import vrml2csv
>>> from vrml2csv import vrml2csv
>>> root = '/Users/usrname/dir/root-of-your-vrml'
>>> f=open(root+'.wrl')
>>> vrml2csv(f,root)
Reading vertex coordinates.
Reading normal vectors.
Reading coordinate indices.
...
```
