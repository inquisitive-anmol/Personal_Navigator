# I have created this
from django.http import HttpResponse
def navigate(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Navigator</title>
    <style>
        body {
            background-color: rgba(220, 20, 60, 0.571);
        }

        h1 {
            color: rgb(8, 98, 128);
            text-align: center;

        }

        hr {
            color: turquoise;
            border: 1px;
        }

        div {
            box-shadow: 10px 10px 5px rgb(30, 148, 187);
        }

        div li a{
            font-size: 3rem;
            color: rgb(114, 44, 70);
            text-decoration: none;
        }
        div li a:hover{
            color: rgb(57, 4, 4);
        }
        p{
            font-size: larger;
            text-align: center;
        }
    </style>
</head>

<body>
    <h1>Welcome to Personal Navigator</h1>
    <div>
    <p>All your quick navigating links are here!!!!</p>
    </div>
    <div>
        <ul>
            <li><a href = "https://www.google.com">Google</a></li>
            <li><a href="https://www.youtube.com">youtube</a>

            </li>
            <li>
                <a href="https://www.flipkart.com">flipkart</a>
            </li>
            <li>
                <a href="https://www.w3schools.com">w3schools</a>
            </li>
        </ul>
    </div>

</body>

</html> """)