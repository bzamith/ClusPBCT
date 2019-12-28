if(!exists("foo", mode="function")) source("hierarchy.R")

rtnDataset=function(approach,classes){ #returnDataset according to the approach
  if(approach=="path"||approach=="PATH"||approach=="Path"){
    featuresMatrix=pathApproach(classes)
  }
  else if(approach=="children"||approach=="CHILDREN"||approach=="Children"){
    featuresMatrix=childrenApproach(classes)
  }
  else if(approach=="depth"||approach=="DEPTH"||approach=="Depth"){
    featuresMatrix=depthApproach(classes)
  }
  return(featuresMatrix)
}

pathApproach=function(classes){
  refTable=matrix(nrow=1,ncol=length(classes))  #refTable (can be outputed)
  refTable[1,]=1:length(classes)
  colnames(refTable)=classes
  pathMatrix=matrix("0",nrow=length(classes),ncol=length(classes)) #output matrix = pathApproach
  rownames(pathMatrix)=classes
  colnames(pathMatrix)=1:length(classes)
  for(i in 1:nrow(pathMatrix)){
    ancestors=c(classes[i],ancestorTotal(classes[i]))
    for(j in 1:length(ancestors)){
      pathMatrix[i,grep(paste("^",ancestors[j],"$",sep=""),classes)]="1"
    }
  }
  return(pathMatrix)
}

childrenApproach=function(classes){
  refTable=matrix(nrow=1,ncol=length(classes))  #refTable 
  refTable[1,]=1:length(classes)
  colnames(refTable)=classes
  childrenMatrix=matrix("0",nrow=length(classes),ncol=length(classes)) #output matrix = childrenApproach
  rownames(childrenMatrix)=classes
  colnames(childrenMatrix)=1:length(classes)
  for(i in 1:nrow(childrenMatrix)){
    children=c(classes[i],childrenTotal(classes[i],classes))
    for(j in 1:length(children)){
      childrenMatrix[i,grep(paste("^",children[j],"$",sep=""),classes)]="1"
    }
  }
  return(childrenMatrix)
}

depthApproach=function(classes){
  depth=depthHierarchy(classes)
  depthMatrix=matrix("0",nrow=length(classes),ncol=depth) #output matrix = depthApproach
  rownames(depthMatrix)=classes
  colnames(depthMatrix)=sprintf("L%d", 1:depth)
  for(i in 1:nrow(depthMatrix)){
    depthMatrix[i,]=depthNodeVector(classes[i],classes)
  }
  return(depthMatrix)
}
