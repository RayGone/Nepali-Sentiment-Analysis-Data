index = null;
time = 0;
count = 0;
console.log((count==0) ? 0 : Math.ceil(time/count))
setInterval(function(){
    time+=1
    var speed = (count==0) ? 0 : Math.ceil((count*60)/time)
    document.getElementById('time').innerHTML = "Time Elapsed: "+time + " sec";
    document.getElementById('count').innerHTML = "Labeled Item: "+count + " items";
    document.getElementById('stat').innerHTML = "Labeling Speed: " + speed + " item/min"
},1000)

function getText(){
    fetch("/get_next_item").
        then(response => response.json()).
            then(data => {
                if('error' in data){
                    document.getElementById('text').innerHTML = "No Data to Label"
                }else{
                    index = data.index
                    document.getElementById('text').innerHTML = data['data'][data['txt-col-name']]
                    document.getElementById('info').innerHTML = "Remaining: "+data['remaining']+", Labeled: "+(data['total']-data['remaining'])
                }
            })
}

function setLabel(label){
    count+=1
    console.log(JSON.stringify({'index':index,'label': label}))
    document.getElementById('text').innerHTML = `<i class="fa-solid fa-spinner fa-spin-pulse" style='font-size:3em'></i>`
    fetch(`/set_label`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({'index':index,'label': label})
      }).then(
        response => {
            getText();
        }
    )
}

getText();

// document.getElementById('btn-pos').addEventListener('click',setLabel(1));
// document.getElementById('btn-neg').addEventListener('click',setLabel(2));
// document.getElementById('btn-neu').addEventListener('click',setLabel(0));