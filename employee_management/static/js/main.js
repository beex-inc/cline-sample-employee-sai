// Load employees when the page loads
document.addEventListener('DOMContentLoaded', loadEmployees);

// Function to load all employees
function loadEmployees() {
    fetch('/api/employees')
        .then(response => response.json())
        .then(employees => {
            const employeeList = document.getElementById('employeeList');
            employeeList.innerHTML = '';

            employees.forEach(employee => {
                employeeList.innerHTML += `
                    <tr>
                        <td>${employee.employee_number}</td>
                        <td>${employee.name}</td>
                        <td>${employee.email}</td>
                        <td>${employee.department}</td>
                        <td>${employee.hire_date}</td>
                        <td>
                            <button class="btn btn-sm btn-info" onclick="editEmployee(${employee.id})">編集</button>
                            <button class="btn btn-sm btn-danger" onclick="deleteEmployee(${employee.id})">削除</button>
                        </td>
                    </tr>
                `;
            });
        })
        .catch(error => console.error('Error:', error));
}

// Show employee form for creating new employee
function showEmployeeForm() {
    document.getElementById('employeeForm').reset();
    document.getElementById('employeeId').value = '';
    document.getElementById('modalTitle').textContent = '社員情報登録';
    $('#employeeModal').modal('show');
}

// Edit employee
function editEmployee(id) {
    fetch(`/api/employees/${id}`)
        .then(response => response.json())
        .then(employee => {
            document.getElementById('employeeId').value = employee.id;
            document.getElementById('employeeNumber').value = employee.employee_number;
            document.getElementById('name').value = employee.name;
            document.getElementById('email').value = employee.email;
            document.getElementById('department').value = employee.department;
            document.getElementById('hireDate').value = employee.hire_date;
            document.getElementById('modalTitle').textContent = '社員情報編集';
            $('#employeeModal').modal('show');
        })
        .catch(error => console.error('Error:', error));
}

// Save employee (create or update)
function saveEmployee() {
    const employeeId = document.getElementById('employeeId').value;
    const employeeData = {
        employee_number: document.getElementById('employeeNumber').value,
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        department: document.getElementById('department').value,
        hire_date: document.getElementById('hireDate').value
    };

    const url = employeeId ? `/api/employees/${employeeId}` : '/api/employees';
    const method = employeeId ? 'PUT' : 'POST';

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(employeeData)
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                $('#employeeModal').modal('hide');
                loadEmployees();
                alert(data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('エラーが発生しました。');
        });
}

// Delete employee
function deleteEmployee(id) {
    if (confirm('この社員情報を削除してもよろしいですか？')) {
        fetch(`/api/employees/${id}`, {
            method: 'DELETE'
        })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    loadEmployees();
                    alert(data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('エラーが発生しました。');
            });
    }
}
