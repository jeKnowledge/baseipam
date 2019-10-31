let step = 'step1';

function next() {
  const step1 = document.getElementById('step1');
  const step2 = document.getElementById('step2');
  const step3 = document.getElementById('step3');
  var desc = document.getElementById('prog_desc');

  if (step === 'step1') {
    step = 'step2';
    step1.classList.add("active");
    desc.innerHTML= "Comunicação e acompanhamento contínuos da empresa com a equipa, de forma a assegurar que o trabalho vai de encontro à realidade da empresa.";

  } else if (step === 'step2') {
    step = 'step3';
    step2.classList.add("active");
    step3.classList.add("active");
    desc.innerHTML= "Finalização e entrega do projeto final.";

  } else if (step === 'step3') {
    step = 'step1';
    step1.classList.remove("active");
    step2.classList.remove("active");
    step3.classList.remove("active");
    desc.innerHTML= "Análise da situação atual da empresa e identificação das suas necessidades.";
  }
}
