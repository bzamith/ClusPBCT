options(java.parameters = "-Xmx8000m")
options(warn = -1) 

jgc <- function()
{
  gc()
  .jcall("java/lang/System", method = "gc")
}


#SCRIPT TO CREATE THE TWO INTERACTION DATA DATASETS
#INPUT: FILE (ARFF) AND //APPROACH (PATH, CHILDREN OR DEPTH)

createIntDatasets=function(file,path=TRUE,depth=TRUE,children=TRUE){
  require("RWeka")
  file=paste("datasets/",file,sep="")
  if(!exists("foo", mode="function")) source("featuresApproaches.R")
  if(!exists("foo", mode="function")) source("hierarchy.R")

  con = file(file, "r") #open the file
  dataDidntBegin=TRUE #data didnt begin yet 
  nLines=0 #number of lines until it finds the data
  attributes=c() #attributes names
  attrTypes=c() #attributes types numeric or not
  while (dataDidntBegin){ #while data dont begin
    line = readLines(con, n = 1) #read each line
    if(gregexpr("@DATA",line)!=-1){ #if it finds "@DATA", stop
      dataDidntBegin=FALSE
    }
    else if(gregexpr("@ATTRIBUTE",line)!=-1){ #if it finds "@ATRRIBUTE" 
      if(gregexpr("@ATTRIBUTE class",line)==-1){ #and it isnt the class
        spaces=unlist(gregexpr(" ",line)) 
        attributes=c(attributes,substr(line,spaces[1]+1,spaces[2]-1)) #attributes names are saved
        if(substr(line,spaces[length(spaces)]+1,nchar(line))=="numeric"){
          attrTypes=c(attrTypes,"1") #numeric
        }
        else if(substr(line,spaces[length(spaces)]+1,spaces[length(spaces)]+1)=="{"){
          attrTypes=c(attrTypes,"2") #factors
        }else{
          attrTypes=c(attrTypes,"0")
        }
      } else{ #if it is the class
        spaces=unlist(gregexpr(" ",line))
        classes=substr(line,spaces[length(spaces)]+1,nchar(line))
        classes=unlist(strsplit(classes, ",", fixed = FALSE, perl = FALSE, useBytes = FALSE)) #classes are saved
      }              
    }
    else if ( length(line) == 0 ) {
      break
    }
    nLines=nLines+1
  }
  data=read.table(file,sep=",",skip=nLines,stringsAsFactors=FALSE) #read the input dataset
  close(con)
  
  rm(spaces,con,line,nLines,dataDidntBegin) #current: data, attributes and classes
  colnames(data) = c(attributes,"class")

  intD1 = matrix("0",nrow=nrow(data),ncol=length(classes)) #creates the interaction data 1 matrix
  colnames(intD1)=classes
  rownames(intD1)=sprintf("Protein%d", 1:nrow(intD1))

  #constructs the interaction data 1
  for(i in 1:length(classes)){
    ancestors=c(classes[i],ancestorTotal(classes[i])) #levando em consideracao os ancestrais
    pos=grep(paste("^",classes[i],"$",sep=""),data[,"class"])
    pos=c(pos,grep(paste("^",classes[i],"@",sep=""),data[,"class"]))
    pos=c(pos,grep(paste("@",classes[i],"$",sep=""),data[,"class"]))
    pos=c(pos,grep(paste("@",classes[i],"@",sep=""),data[,"class"]))
    if(length(pos)>0){
      for(j in 1:length(ancestors)){
        column=grep(paste("^",ancestors[j],"$",sep=""),classes)
        intD1[pos,column]="1"
      }
    }
  }
  rm(i,j,ancestors) #current: data, classes, attributes and intD1

  #interaction data 2 = transposed matrix
  intD2=t(intD1)

  #intD1
  data=data[,-ncol(data)]
  #make numeric
  for(i in 1:ncol(data)){
    if(attrTypes[i]=="1"){
      data[,i]=as.numeric(data[,i])
    }
    else if(attrTypes[i]=="2"){
      data[,i]=as.factor(data[,i])
    }
  }
  
  intD1=data.frame(data,intD1,check.names = FALSE)
  write.arff(intD1,paste("intD1",substr(file,10,nchar(file)),sep="_"),eol="\n")
  #intD2
  if(path==TRUE){
    intD2PATH=data.frame(rtnDataset("PATH",classes),intD2,check.names = FALSE)
    write.arff(intD2PATH,paste("intD2_Path",substr(file,10,nchar(file)),sep="_"),eol="\n")
  }
  if(depth==TRUE){
    intD2DEPTH=data.frame(rtnDataset("DEPTH",classes),intD2,check.names = FALSE)
    write.arff(intD2DEPTH,paste("intD2_Depth",substr(file,10,nchar(file)),sep="_"),eol="\n")
  }
  if(children==TRUE){
    intD2CHILDREN=data.frame(rtnDataset("CHILDREN",classes),intD2,check.names = FALSE)
    write.arff(intD2CHILDREN,paste("intD2_Children",substr(file,10,nchar(file)),sep="_"),eol="\n")
  }

  utils::View(intD1)
  utils::View(intD2)
}

#Make corrections on factors (they need to be numeric)
corrDatasets=function(file){
  x <- readLines(file)
  y <- gsub( "\\{0\\}", "numeric", x)
  y <- gsub( "\\{1\\}", "numeric", y)
  y <- gsub( "\\{0,1\\}", "numeric", y)
  writeLines(y, con = file)
}

#Run to generate the files
run=function(file,path=TRUE,depth=TRUE,children=TRUE){
  createIntDatasets(file,path,depth,children)
  corrDatasets(paste("intD1",file,sep="_"))
  if(path){
    corrDatasets(paste("intD2_Path",file,sep="_"))
  }
  if(depth){
    corrDatasets(paste("intD2_Depth",file,sep="_"))
  }
  if(children){
    corrDatasets(paste("intD2_Children",file,sep="_"))
  }
}

run("cellCycle_FUN.train.arff",depth=FALSE)
#run("church_FUN.train.arff",path=FALSE,children=FALSE)

