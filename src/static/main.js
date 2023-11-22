import semesterData from './session.json' assert {type: 'json'};

const url = 'http://127.0.0.1:5001/api/run_program';  // URL according to your Flask app
fetch(url)

async function fetchData(){

    try{
        const response = await fetch('http://127.0.0.1:5001/api/get_semester');
        const data = await response.json();
        
        return data; // Return the fetched data
    
    }catch(error){
        console.error('Error:', error);
    };

}

let radius = 200;
const courseTree = document.getElementById('courseTree');
var circles = [];
const circlesContainer = document.getElementById('circles-container');
const linesContainer = document.getElementById('lines-container');

function calculateCircularPath(radius, numPoints) {
    const coordinates = [];

    for (let i = 0; i < numPoints; i++) {
      const angle = (i / numPoints) * 2 * Math.PI;
      const x = radius * Math.cos(angle)+50;        //50 for margin size
      const y = radius * Math.sin(angle)+50;
      coordinates.push({ x, y });
    }

    return coordinates;
  }

//const semesterData = await fetchData()
//console.log(semesterData)
const pathCoordinates = calculateCircularPath(radius, Object.keys(semesterData).length-1);


function getId(courseName){
    let id=-1;
    for (const c in semesterData){
        const course = semesterData[c];
        if (course["nom"] == courseName){
            return course["id"];
        }
    }
    
}

// Function to draw a course node
function drawCourseNode(course, x, y) {
    const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    circle.setAttribute('cx', x);
    circle.setAttribute('cy', y);
    circle.setAttribute('r', 20);
    circle.setAttribute('fill', 'lightblue');

    const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    text.setAttribute('x', x);
    text.setAttribute('y', y + 5);
    text.setAttribute('text-anchor', 'middle');
    text.textContent = course.nom;

    circles.push([circle, text]);

}

// Function to draw an arc between two courses
function drawArc(x1, y1, x2, y2) {
    const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line.setAttribute('x1', x1);
    line.setAttribute('y1', y1);
    line.setAttribute('x2', x2);
    line.setAttribute('y2', y2);
    line.setAttribute('stroke', 'gray');
    line.setAttribute('stroke-width', 2);

    linesContainer.appendChild(line);
}

//create circles with text objects to be stored in an array
let i = 0;
for (const courseId in semesterData) {
    if (courseId.startsWith("cours")) {
        const course = semesterData[courseId];
        let x = pathCoordinates[i].x; let y = pathCoordinates[i].y;
        drawCourseNode(course, x+radius, y+radius);

        i += 1;
    }
}

// Draw the courses and arcs
for (const i in circles){
    const element = circles[i];
    circlesContainer.appendChild(element[0]);
    circlesContainer.appendChild(element[1]);
} 

 // Draw arcs for dependencies
 let j = 0;
 for (const courseId in semesterData) {
    if (courseId.startsWith("cours")) {
        const course = semesterData[courseId];
        course.adjacences.forEach(dependency => {
            const id = getId(dependency);
            drawArc(circles[course["id"]][0].getAttribute('cx'), circles[course["id"]][0].getAttribute('cy'), circles[id][0].getAttribute('cx'), circles[id][0].getAttribute('cy'));
        });
        j += 1;
    }
}