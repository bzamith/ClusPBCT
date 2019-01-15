#ANCESTOR TOTAL, "/"
ancestorTotal<-function(node){
  t<-c()
  value<-regexpr("\\/[^\\/]*$", node)[1]
  while(value!="-1"){
    node<-substr(node,1,value-1)
    t<-c(t,node)
    value<-regexpr("\\/[^\\/]*$", node)[1]	
  }
  return(t)
}

#DEPTH HIERARCHY, "/"
depthHierarchy<-function(classes){
  depth=0
  for(i in 1:length(classes)){
    value=lengths(regmatches(classes[i], gregexpr("/", classes[i])))
    if(value>depth){
      depth=value
    }
  }
  return(depth+1)
}


#DEPTH NODE VECTOR, "/"
depthNodeVector<-function(node,classes){
  depth=depthHierarchy(classes)
  depthNode=lengths(regmatches(node, gregexpr("/", node)))
  return(c(rep("1",depthNode+1),rep("0",(depth-depthNode-1))))
}

#CHILDREN TOTAL
childrenTotal<-function(node,classes){
  t<-c()
  for(i in 1:length(classes))
    if(nchar(classes[i])>nchar(node))
      if(substr(classes[i],1,(nchar(node)+1))==paste(node,"/",sep=""))
        t<-c(t,classes[i])
      if(identical(t, character(0)))
        return()
      else
        return(unique(t))
}
