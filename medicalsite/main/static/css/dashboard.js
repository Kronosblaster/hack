
window.onload = function () {
    var elem=document.getElementById("chat")
    r=elem.style.backgroundImage
    elem.addEventListener('click', chatbot)
  };

function chatbot(){  

    var elem=document.getElementById("chat")
            if(elem.style.backgroundImage == r){
            elem.style.backgroundImage = "url('"+r_clicked+"')"
            }
            else{
            elem.style.backgroundImage = r 
            }       
        }

  
  
      const url1='getMedData/';
      
      function dataGet_User(url,table_name){
      data=fetch(url).then(data=>{return data.json()}).then(
      data=>{
        console.log(data)
         var table=document.getElementById(table_name)
          for(i=0;i<data.length;i++){
            
            row = document.createElement("tr");
            cellA = document.createElement("td");
            cellL=document.createElement("td");
            cellE=document.createElement("td");
  
            var id=data[i].med_id
  
            char1=document.createElement("text");
            char1.innerHTML=" | "
  
            view=document.createElement("a");
            view.innerHTML="View"
            view.id=id+"_view"
            view.href="myMed?id="+view.id
  
            remove=document.createElement("a");
            remove.innerHTML="Remove"
            remove.id=id+"_remove"
            remove.href="myMed?id="+remove.id
  
            date=document.createElement("td");
            date.innerHTML=data[i].posted_on
            cellE.appendChild(date);
            
            
            cellL.appendChild(view)
            cellL.appendChild(char1)
            cellL.appendChild(remove)
  
            cellA.innerHTML=data[i].title
            
            table.appendChild(row);
            row.appendChild(cellA);
            row.appendChild(cellL);
            row.appendChild(cellE);
            
             }
  
            } )
              }
      dataGet_User(url1,"med_table")
    
  