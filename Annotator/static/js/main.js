index = null;

function getText(){
    fetch("/get_next_item").
        then(response => response.json()).
            then(data => {
                if('error' in data){
                    document.getElementById('text').innerHTML = "No Data to Label"
                }else{
                    index = data.index
                    document.getElementById('text').innerHTML = data['data']['Text']
                    document.getElementById('info').innerHTML = "Remaining Unlabeled Data: "+data['remaining']
                }
            })
}

function setLabel(label){
    fetch(`/set_label/${index}/${label}`).then(
        response => {
            getText();
        }
    )
}

getText();

// document.getElementById('btn-pos').addEventListener('click',setLabel(1));
// document.getElementById('btn-neg').addEventListener('click',setLabel(2));
// document.getElementById('btn-neu').addEventListener('click',setLabel(0));