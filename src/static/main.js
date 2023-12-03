//import semesterData from './session.json' assert {type: 'json'};
//import colorData from './color_picker.json' assert {type: 'json'};

//const url = 'http://127.0.0.1:5001/api/run_program';  // URL according to your Flask app
const flask_url = 'http://127.0.0.1:5001/api/';
const run_url = 'run_program';
const get_semester_url = 'get_semester';
const get_color_url = 'get_colorPicker';
fetch(flask_url + run_url)

let semesterData;
let pathCoordinates;
let colorData;
async function fetchData(){

    try{
        const response = await fetch(flask_url+get_semester_url);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        semesterData = await response.json();
        pathCoordinates = calculateCircularPath(radius, Object.keys(semesterData).length-1);
        
        const colorResponse = await fetch(flask_url+get_color_url);
        if (!colorResponse.ok) {
            throw new Error(`HTTP error! Status: ${colorResponse.status}`);
        }
        colorData = await colorResponse.json();

        next();     //proceed to next block of code AFTER all data is successdully loaded
    
    }catch(error){
        console.error('Error fetching data:', error);
        throw error;
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

fetchData();

function next(){
    const sortedMap = new Map(Object.entries(semesterData).sort(([, a], [, b]) => a.id - b.id));

    function getId(courseName){
        let id=-1;
        for (const c in semesterData){
            const course = semesterData[c];
            if (course["nom"] == courseName){
                return course["id"];
            }
        }
        
    }

    // Function to draw smal dot
    function createDot(x,y){
        const dot = document.createElementNS("http://www.w3.org/2000/svg", 'circle');
        const r=2;
        const fill='black';

        dot.setAttribute("cx",x);
        dot.setAttribute("cy",y);
        dot.setAttribute("r",r);
        dot.style.fill = fill;
        
        return dot;
    }

    // Function to draw a course node
    function drawCourseNode(course, x, y) {
        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('id', 'cours'+course['id']);
        circle.setAttribute('cx', x);
        circle.setAttribute('cy', y);
        circle.setAttribute('r', 10);
        const colorId = course["couleur"]
        circle.setAttribute('fill', colorData[colorId]);

        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', x);
        text.setAttribute('y', y + 5);
        text.setAttribute('text-anchor', 'middle');
        text.setAttribute("font-size", "7");
        text.textContent = course.nom;

        circles.push([circle, text]);

    }

    // Function to draw an arc between two courses
    function drawArc(x1, y1, x2, y2, n) {
        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('id', n);
        line.setAttribute('class', 'arc');

        line.setAttribute('x1', x1);
        line.setAttribute('y1', y1);
        line.setAttribute('x2', x2);
        line.setAttribute('y2', y2);
        line.setAttribute('stroke', 'gray');
        line.setAttribute('stroke-width', 2);

        const startDot = createDot(x1, y1);
        const endDot = createDot(x2, y2);

        linesContainer.appendChild(startDot);
        linesContainer.appendChild(line);
        linesContainer.appendChild(endDot);
    }

    //create circles with text objects to be stored in an array
    let i = 0;
    for (const courseId of sortedMap.keys()) {
        if (courseId.startsWith("cours")) {
            const course = sortedMap.get(courseId);
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
    let numArcs = 0;
    for (const courseId of sortedMap.keys()) {
        if (courseId.startsWith("cours")) {
            const course = sortedMap.get(courseId);
            course.adjacences.forEach(dependency => {
                const id = getId(dependency);
                drawArc(circles[course["id"]][0].getAttribute('cx'), circles[course["id"]][0].getAttribute('cy'), circles[id][0].getAttribute('cx'), circles[id][0].getAttribute('cy'), numArcs);
                numArcs += 1;
            });
        }
    }
    dynamics(sortedMap);
}


function dynamics(sortedMap){ 
    function getName(id){

    }

    function adjacencesToString(courseId){
        //return sortedMap.get(courseId).adjacences.map((id) => {return getName(id)}).join(", ");
        return sortedMap.get(courseId).adjacences;
    } 

    // Attach an event listener to the common ancestor
    linesContainer.addEventListener('mouseover', function(event) {
        // Get the target element that triggered the event
        var target = event.target;

        // Check if the target is a line element
        if (target.tagName === 'line') {
        // Change the style of the hovered line
        target.style.stroke = '#4f4c4c';
        target.style.strokeWidth = '3';

        // Change the style of other lines with the shared class
        var dataLines = document.querySelectorAll('.arc');
        dataLines.forEach(function(line) {
            if (line !== target) {
            line.style.stroke = '#b8b6b6';
            line.style.strokeWidth = '1';
            }
        });
        }
    });

    linesContainer.addEventListener('mouseout', function(event) {
        // Restore styles when the mouse leaves the line
        var target = event.target;
        if (target.tagName === 'line') {
        target.style.stroke = 'gray';
        target.style.strokeWidth = '2';

        // Restore styles of other lines with the shared class
        var dataLines = document.querySelectorAll('.arc');
        dataLines.forEach(function(line) {
            line.style.stroke = 'gray'; // Use the original color of your data lines
            line.style.strokeWidth = '2'; // Use the original stroke width of your data lines
        });
        }
    });

  
    var popup; // Variable to store the popup element

    circlesContainer.addEventListener('mouseover', function(event) {
        // Make sure we eork only with circles
        if (event.target.tagName == "circle"){

            const target = event.target;
            const id = target["id"];

            // Create a div element for the popup
            popup = document.createElement('div');

            // Set initial properties for the popup
            popup.className = 'popup';
            popup.style.display = 'none'; // Initially hide the popup

            // Get the coordinates of the hover event
            var x = event.clientX;
            var y = event.clientY;

            // Set the position of the popup near the hover coordinates
            popup.style.left = x + 'px';
            popup.style.top = y + 'px';

            // Set the content of the popup
            popup.textContent = "Adjacences: " + "\n" + adjacencesToString(id);

            // Append the popup to the body
            document.body.appendChild(popup);
            
            // Show the popup
            popup.style.display = 'block';
        }
    });

    circlesContainer.addEventListener('mousemove', function(event) {
        // Update the position of the popup as the mouse moves
        if (popup) {
        var x = event.clientX;
        var y = event.clientY;

        popup.style.left = x + 'px';
        popup.style.top = y + 'px';
        }
    });

    circlesContainer.addEventListener('mouseout', function() {
        // Remove the popup when the mouse leaves the SVG container
        if (popup) {
        document.body.removeChild(popup);
        popup = null;
        }
    });
}