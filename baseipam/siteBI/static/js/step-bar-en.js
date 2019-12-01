let step = 'step1';

function next() {
  const step2 = document.getElementById('step2');
  const step3 = document.getElementById('step3');
  var desc = document.getElementById('progressDescription');

  if (step === 'step1') {
    step = 'step2';
    step2.classList.add("active");
    desc.innerHTML= "Continuous communication and monitoring of the team by the company in order to assure that the workmeets the company’s reality.";

  } else if (step === 'step2') {
    step = 'step3';
    step3.classList.add("active");
    desc.innerHTML= "Finalization and final delivery of the project.";

  } else if (step === 'step3') {
    step = 'step1';
    step2.classList.remove("active");
    step3.classList.remove("active");
    desc.innerHTML= "Analysis of the current situation of the company and identification of its needs.";
  }
}
