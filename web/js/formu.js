const guardarEstudiante = document.querySelector('#guardarEstudiante');
let estudiante = [];
let editar = false; 
window.addEventListener("DOMContentLoaded", async () => {
    const response = await fetch("/getlist/formulario");
    const data = await response.json();
    estudiante = data;
//  generarEstudiante(estudiante);

})

guardarEstudiante.addEventListener("submit", async (e) => {
    e.preventDefault();
//   const id           = guardarEstudiante["id_est"].value;
    const cedula       = guardarEstudiante["ced"].value;
    const nombres      = guardarEstudiante["nomb"].value;
    const apellidos    = guardarEstudiante["apell"].value;
    const correo       = guardarEstudiante["correo"].value;
    const celular      = guardarEstudiante["celu"].value;
    const telefono     = guardarEstudiante["tele"].value;
    const ciudad       = guardarEstudiante["ciu"].value;
    const sector       = guardarEstudiante["sect"].value;
    const barrio       = guardarEstudiante["barr"].value;
    const movilizacion = guardarEstudiante["mov"].value; 
    if (!editar){
        const responde=await fetch("/save/formulario",{
            method: "POST",
            headers: {"Content-Type":"aplication/json",},
            body: JSON.stringify({
                //id,
                cedula,
                nombres,
                apellidos,
                correo,
                celular,
                telefono,
                ciudad,
                sector,
                barrio,
                movilizacion
            }),
        });
        const data = await responde.json();
        estudiante.push(data);
//        generarEstudiante(estudiante); 
    }
});

