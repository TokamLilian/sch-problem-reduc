import data from './session.json' assert {type: 'json'};
//const data = {"cours0": {"nom": "IFT 1005", "heures": 4, "adjacences": []}, "cours1": {"nom": "IFT 1015", "heures": 4, "adjacences": []}, "cours2": {"nom": "IFT 1215", "heures": 4, "adjacences": []}, "cours3": {"nom": "IFT 2105", "heures": 4, "adjacences": ["IFT 2505", "MAT 1978", "IFT 1025", "IFT 3395", "IFT 3305", "MAT 1400", "MAT 1600"]}, "cours4": {"nom": "IFT 2505", "heures": 4, "adjacences": ["MAT 1978", "IFT 2105", "IFT 1025", "MAT 1400", "MAT 1600"]}, "cours5": {"nom": "IFT 3395", "heures": 4, "adjacences": ["IFT 2105", "IFT 3305"]}, "cours6": {"nom": "IFT 1025", "heures": 4, "adjacences": ["IFT 2505", "MAT 1978", "IFT 2105"]}, "cours7": {"nom": "IFT 2255", "heures": 4, "adjacences": ["IFT 4000", "IFT 3265"]}, "cours8": {"nom": "MAT 1400", "heures": 6, "adjacences": ["IFT 2105", "IFT 2505", "MAT 1600"]}, "cours9": {"nom": "MAT 1600", "heures": 6, "adjacences": ["MAT 1400", "IFT 2105", "IFT 2505"]}, "cours10": {"nom": "MAT 1978", "heures": 6, "adjacences": ["IFT 2505", "IFT 2105", "IFT 1025"]}, "cours11": {"nom": "IFT 3265", "heures": 4, "adjacences": ["IFT 4000", "IFT 2255"]}, "cours12": {"nom": "IFT 3305", "heures": 4, "adjacences": ["IFT 2105", "IFT 3395"]}, "cours13": {"nom": "IFT 4000", "heures": 4, "adjacences": ["IFT 2255", "IFT 3265"]}, "periodes": 0}
//console.log(data)

let radius = 200;
const courseTree = document.getElementById('courseTree');
var circles = [];
const circlesContainer = document.getElementById('circles-container');
const linesContainer = document.getElementById('lines-container');

function calculateCircularPath(radius, numPoints) {
    const coordinates = [];

    for (let i = 0; i < numPoints; i++) {
      const angle = (i / numPoints) * 2 * Math.PI;
      const x = radius * Math.cos(angle);
      const y = radius * Math.sin(angle);
      coordinates.push({ x, y });
    }

    return coordinates;
  }

const pathCoordinates = calculateCircularPath(radius, Object.keys(data).length-1);


function getId(courseName){
    let id=-1;
    for (const c in data){
        const course = data[c];
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
    //circlesContainer.appendChild(circle);
    //circlesContainer.appendChild(text);
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
for (const courseId in data) {
    if (courseId.startsWith("cours")) {
        const course = data[courseId];
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
 for (const courseId in data) {
    if (courseId.startsWith("cours")) {
        const course = data[courseId];
        course.adjacences.forEach(dependency => {
            const id = getId(dependency);
            drawArc(circles[course["id"]][0].getAttribute('cx'), circles[course["id"]][0].getAttribute('cy'), circles[id][0].getAttribute('cx'), circles[id][0].getAttribute('cy'));
        });
        j += 1;
    }
}