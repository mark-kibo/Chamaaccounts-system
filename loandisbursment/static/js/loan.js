function createelement(value){
    let form1= document.getElementById('loan');
    console.log(form1);
    if (document.getElementById('amount')){
        document.getElementById('amount').remove();
    }
    if (document.getElementById('amount2')){
        document.getElementById('amount2').remove();
    }
    if (document.querySelector('p')){
        document.querySelector('p').remove();
    }
    let input1 = document.createElement('input');
    let input2 = document.createElement('input');
    let button1= document.createElement('button')
    let p = document.createElement('p');
    let p1 = document.createElement('p');
    input1.setAttribute('type', 'text');
    input1.setAttribute('name', 'paid');
    input1.setAttribute('id', 'amount');
    input2.setAttribute('type', 'text');
    input2.setAttribute('name', 'loaned')
    input2.setAttribute('id', 'amount2');
    p.setAttribute('class', 'amount')
    button1.setAttribute('type', 'submit');
    button1.setAttribute('class', 'btn btn-primary');

    
    p.innerHTML="Paid amount";
    p1.innerHTML="loaned amount";
    button1.innerHTML="submit";

    if (value == "pay")
    {
        form1.appendChild(p);
        form1.appendChild(input1);

    }
    if (value == "get_loan")
    {
        form1.appendChild(p1);
        form1.appendChild(input2);
        

    }
    form1.appendChild(button1);
}
