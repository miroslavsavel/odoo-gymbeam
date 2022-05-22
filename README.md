# Case Study - Odoo developer

## 1. TASK: Create a new boolean field i_love_gb on the Employee screen after the work_email field.
    - Find out how the model of employee is named.
    - Find out how the view of the employee form is named. (hint: find out how developer
    mode is activated in Odoo, then via this menu item ‘edit view:form’ structure and name/id
    of the view can be found, there are also other ways)
    - Override employee model/view to add new field
    - Install your new module

## DONE

![alt text](https://i.ibb.co/vDGSzG6/1.png)


## 2. TASK: Create 3 new Integer fields salary, tax and total_salary.
-  Field total_salary should be automatically set to value salary + tax. New fields should be after the address field on the Private information tab. (hint: onchange, depends, compute...)

## DONE
![alt text](https://i.ibb.co/mF0wymW/2.png)


## 3. TASK: Replace phone field with new field special_phone.
- On save action of the employee record, check if the field is empty, if it is empty, set the default value of the field to “0901123456”.

## DONE
![after save](https://i.ibb.co/kc7BPyJ/3b.png)


