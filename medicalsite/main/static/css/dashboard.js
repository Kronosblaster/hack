



      const url1='getMedData/';
      
      function dataGet_User(url,table_name){
      data=fetch(url).then(data=>{return data.json()}).then(
      data=>{
        //console.log(data)
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



window.onload = function () {


  var elem=document.getElementById("chat")
  r=elem.style.backgroundImage

  let recording = false;
  const saveAudio = (blobUrl) => {
    const downloadEl = document.createElement("a");
    downloadEl.style = "display: block";
    downloadEl.innerHTML = "download";
    downloadEl.download = "audio.webm";
    downloadEl.href = blobUrl;
    downloadEl.click();
  };

  const converToBase64 = (blobData) => {
    let reader = new FileReader();
    let base64data;
    reader.readAsDataURL(blobData);
    reader.onloadend = function () {
      // this is the base64 version of the audio
      // it can be sent as a POST request to the server
      base64data = reader.result;
      var t=base64data
      post(t)
      //console.log(base64data);
      
    };
  };

  const recordAudio = () =>
    new Promise(async (resolve) => {
      const stream = await navigator.mediaDevices.getUserMedia({
        audio: true,
      });
      const mediaRecorder = new MediaRecorder(stream);
      const audioChunks = [];

      mediaRecorder.addEventListener("dataavailable", (event) => {
        audioChunks.push(event.data);
      });

      const start = () => mediaRecorder.start();

      const stop = () =>
        new Promise((resolve) => {
          mediaRecorder.addEventListener("stop", () => {
            const audioBlob = new Blob(audioChunks);
            converToBase64(audioBlob); // this function takes the blob and convert it into base64 format

            const audioUrl = URL.createObjectURL(audioBlob);
            //saveAudio(audioUrl);
            const audio = new Audio(audioUrl);
            const play = () => audio.play();
            resolve({ audioBlob, audioUrl, play });
          });

          mediaRecorder.stop();
        });

      resolve({ start, stop });
    });

  const sleep = (time) =>
    new Promise((resolve) => setTimeout(resolve, time));

  let recorder;
  (async () => {
    recorder = await recordAudio();
  })();
  document.getElementById("chat").addEventListener("click", async (e) => {
    var elem=document.getElementById("chat")
    if (!recording) {
      recorder.start();
      
      elem.style.backgroundImage = "url('"+r_clicked+"')"
      recording = true;
    } else {
      recording = false;
      const audio = await recorder.stop();
      elem.style.backgroundImage = r
      // audio.play();
    }
  });
};


function post(data){
  
  var url = "http://127.0.0.1:8000/user/dashboard/record/";
  var xhr = new XMLHttpRequest();
  xhr.onload = () => {

    // print JSON response
    if (xhr.status >= 200 && xhr.status < 300) {
        // parse JSON
        const response = JSON.parse(xhr.responseText);
        console.log(response);
    }
};


  xhr.open("POST", url);
  xhr.setRequestHeader('Content-Type', 'application/json');
  const json = {"data":data}
  var data = JSON.stringify(json);
  xhr.send(data);

}



