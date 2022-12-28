function add_form(){
    let div = document.getElementById('addcont');
    let form1 =document.createElement('form');
    form1.setAttribute('method', 'post');

    let name = document.createElement('input');
    name.setAttribute('type', 'text');
    name.setAttribute('name', 'Name');

    let br = document.createElement('br');

    let button = document.createElement('button');
    button.setAttribute('type', 'submit');
    button.innerHTML="Submit"

    form1.appendChild(name);
    form1.appendChild(br);
    form1.appendChild(button);

    div.appendChild(form1);
}