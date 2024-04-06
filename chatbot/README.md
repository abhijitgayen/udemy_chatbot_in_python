# About This Project 

This chatbot employs a straightforward neural network architecture, ideal for button-based interactions. 
 
# About Model

Machines primarily understand numerical data, such as vectors and matrices, and not natural language text directly. 

For our project, we are employing a straightforward text-to-vector representation method known as "bag of words." This approach allows us to convert text data into numerical vectors, enabling the machine to process and work with the information effectively.

*What is bag of words ?*
```
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
```

we use only two hidden layers of neural networks

```python
class TranNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(TranNet, self).__init__()
                 
        self.fc1 = nn.Linear(input_size, hidden_size) 
        self.fc2 = nn.Linear(hidden_size, hidden_size) 
        self.fc3 = nn.Linear(hidden_size, num_classes)
        
        self.relu =  nn.ReLU()
    
    def forward(self, x):
        
        out = self.fc1(x)
        out = self.relu(out)      
        out = self.fc2(out)
        out = self.relu(out)
        out = self.fc3(out)
        
        return out
```
Each neuron node within our model is associated with an activation function. In this specific project, we have chosen to use the Rectified Linear Unit (ReLU) activation function.


# SetUp Error for this project
if you fail try to install Pytorch separately. (Noted that fast comment out Pytorch)
To install Pytorch in your system.
(Link)[https://pytorch.org/get-started/locally/]

 
