(function(){
  var $=function(id){return document.getElementById(id)};
  var m0=new Intl.NumberFormat('en-US',{style:'currency',currency:'USD',maximumFractionDigits:0});
  var m2=new Intl.NumberFormat('en-US',{style:'currency',currency:'USD'});
  var form=$('calc-form');if(!form)return;
  function num(id){var v=parseFloat($(id).value);return isNaN(v)||v<0?0:v}
  function calculate(){
    var price=num('price'),down=num('down'),trade=num('trade'),rate=num('rate'),n=parseInt($('term').value,10),tax=num('tax'),fees=num('fees');
    var taxAmt=Math.max(price-trade,0)*tax/100;
    var p=Math.max(price+taxAmt+fees-down-trade,0),r=rate/1200;
    var pmt=r>0?p*r/(1-Math.pow(1+r,-n)):p/n,total=pmt*n,interest=total-p;
    $('monthly').textContent=m2.format(pmt);
    $('r-loan').textContent=m0.format(p);$('r-interest').textContent=m0.format(interest);
    $('r-total').textContent=m0.format(total);$('r-all').textContent=m0.format(total+down+trade);
    $('r-tax').textContent=m0.format(taxAmt);
    var s=total>0?p/total*100:100;
    $('bar-p').style.width=s+'%';
    $('l-p').textContent='Loan amount '+Math.round(s)+'%';$('l-i').textContent='Interest '+Math.round(100-s)+'%';
    var bal=p,rows='',yi=0,yp=0;
    for(var m=1;m<=n;m++){
      var i=bal*r,pr=Math.min(pmt-i,bal);bal=Math.max(bal-pr,0);yi+=i;yp+=pr;
      if(m%12===0||m===n){rows+='<tr><td>Year '+Math.ceil(m/12)+'</td><td>'+m0.format(yp)+'</td><td>'+m0.format(yi)+'</td><td>'+m0.format(bal)+'</td></tr>';yi=0;yp=0}
    }
    $('sched').innerHTML=rows;
  }
  form.addEventListener('input',calculate);
  form.addEventListener('submit',function(e){e.preventDefault();calculate()});
  $('reset').addEventListener('click',function(){setTimeout(calculate,0)});
  calculate();
})();
