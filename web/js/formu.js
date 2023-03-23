//datos estudiante

const guardarEstudiante = document.querySelector('#guardarEstudiante');
let estudiante = [];
let editar = false; 

window.addEventListener("DOMContentLoaded", async () => {
    const response = await fetch("/getlist/formulario");
    const data = await response.json();
    estudiante = data;
})

guardarEstudiante.addEventListener("submit", async (e) => {
    e.preventDefault();
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

    try {
        const response = await fetch("/save/formulario",{
            method: "POST",
            headers: {"Content-Type":"application/json"},
            body: JSON.stringify({
                cedula_est: cedula,
                nombres: nombres,
                apellidos: apellidos,
                correo: correo,
                celular: celular,
                telefono: telefono,
                ciudad: ciudad,
                sector: sector,
                barrio: barrio,
                movilizacion: movilizacion
            })
        });

        if (!response.ok) {
            throw new Error("Error al guardar los datos del estudiante");
        } 

        const data = await response.json();
        estudiante.push(data);

    } catch (error) {
        console.error(error);
    }
});



//datos instituto_estudiante

const guardarInstituto = document.querySelector('#guardarInstituto');
let instituto = [];
let editar1 = false; 

window.addEventListener("DOMContentLoaded", async () => {
    const response = await fetch("/getlist/institucion");
    const data = await response.json();
    instituto = data;
})

guardarInstituto.addEventListener("submit", async (e) => {
    e.preventDefault();
    const nombre       = guardarInstituto["nomb_ins"].value;
    const tipo         = guardarInstituto["tipo"].value;
    const grado        = guardarInstituto["grsm"].value;
    const seccion      = guardarInstituto["secc"].value;
    const anio         = guardarInstituto["lect"].value;
    const notauno        = guardarInstituto["nt1"].value;
    const notados        = guardarInstituto["nt2"].value;

    try {
        const response = await fetch("/save/institucion",{
            method: "POST",
            headers: {"Content-Type":"application/json"},
            body: JSON.stringify({
                nombre,
                tipo,
                grado,
                seccion,
                anio,
                notauno,
                notados 
            })
        });

        if (!response.ok) {
            throw new Error("Error al guardar los datos del instituto");
        } 

        const data = await response.json();
        instituto.push(data);

    } catch (error) {
        console.error(error);
    }
});


//datos representante

// const guardarRepresentante = document.querySelector('#guardarRepresentante');
// let representante = [];
// let editar3 = false; 

// window.addEventListener("DOMContentLoaded", async () => {
//     const response = await fetch("/getlist/formulario");
//     const data = await response.json();
//     instituto = data;
// })

// guardarRepresentante.addEventListener("submit", async (e) => {
//     e.preventDefault();
//     const cedula_re         = guardarRepresentante["ced_re"].value;
//     const nombre_re         = guardarRepresentante["nomb_re"].value;
//     const apellido_re       = guardarRepresentante["ap_re"].value;
//     const correo_re         = guardarRepresentante["correo_re"].value;
//     const celular_re        = guardarRepresentante["cel_re"].value;
//     const telefono_re       = guardarRepresentante["telf_re"].value;

//     try {
//         const response = await fetch("/save/formulario",{
//             method: "POST",
//             headers: {"Content-Type":"application/json"},
//             body: JSON.stringify({
//                 ced_re:    cedula_re,
//                 nomb_re:   nombre_re,
//                 ap_re:     apellido_re,
//                 correo_re: correo_re,
//                 cel_re:    celular_re,
//                 telf_re:   telefono_re,
//             })
//         });

//         if (!response.ok) {
//             throw new Error("Error al guardar los datos del representante");
//         } 

//         const data = await response.json();
//         representante.push(data);

//     } catch (error) {
//         console.error(error);
//     }
// });





// //datos iecaaa

// const guardariecaaa = document.querySelector('#guardariecaaa');
// let iecaaa = [];
// let editar4 = false; 

// window.addEventListener("DOMContentLoaded", async () => {
//     const response = await fetch("/getlist/formulario");
//     const data = await response.json();
//     iecaaa = data;
// })

// guardarRepresentante.addEventListener("submit", async (e) => {
//     e.preventDefault();
//     const estado                = guardarRepresentante["estado"].value;
//     const planificacion         = guardarRepresentante["plan"].value;
//     const inicializacion        = guardarRepresentante["año_i"].value;
//     const llamada               = guardarRepresentante["fecha_ll"].value;
//     const descripcion           = guardarRepresentante["desc"].value;
//     const observacion           = guardarRepresentante["obse"].value;
//     const evaluacion            = guardarRepresentante["eva"].value;

//     try {
//         const response = await fetch("/save/formulario",{
//             method: "POST",
//             headers: {"Content-Type":"application/json"},
//             body: JSON.stringify({
//                 estado:      estado,
//                 plan:        planificacion,
//                 a_i:       inicializacion,
//                 fecha_ll:    llamada,
//                 desc:        descripcion,
//                 obse:        observacion,
//                 eva:         evaluacion,
//             })
//         });

//         if (!response.ok) {
//             throw new Error("Error al guardar los datos de iecaaa");
//         } 

//         const data = await response.json();
//         iecaaa.push(data);

//     } catch (error) { 
//         console.error(error);
//     }
// }); 
 