# Python Properties Showcase

This project provides a clear and concise demonstration of how to effectively use properties in Python. It explores various approaches to attribute management within classes, progressing from traditional getter and setter methods (common in languages like Java or C++) to the more idiomatic Pythonic way using the `@property` decorator.

## Learning Journey

The examples in this repository guide you through an evolution of attribute handling:

1.  **`properties_exemple_01.py`**: Illustrates the classic use of `getX()` and `setX()` methods to access and modify object attributes. This is a familiar pattern for developers coming from other object-oriented languages.
2.  **`properties_exemple_02.py`**: Shows a simplified scenario where, in the absence of validation logic, attributes can be directly set in the constructor. However, this approach offers less control and flexibility.
3.  **`properties_exemple_03.py`**: Introduces the `property()` function. This is a step towards Python's built-in property mechanism, allowing you to associate getter and setter methods with an attribute name, but still explicitly defining those methods.
4.  **`properties_exemple_04.py`**: Demonstrates the most Pythonic and recommended way to define properties using the `@property` decorator for getters and `@<attribute_name>.setter` for setters. This approach leads to cleaner, more readable code, allowing attributes to be accessed as if they were public members while still providing the encapsulation and control of getter/setter methods.

## Why Properties?

Properties in Python offer several advantages:

*   **Encapsulation**: They allow you to control access to an attribute, enabling you to add validation, computation, or logging logic when an attribute is read or written.
*   **Readability**: Code that uses properties often looks cleaner because attribute access doesn't require explicit method calls (e.g., `obj.attribute` instead of `obj.get_attribute()`).
*   **Maintainability**: You can start with simple public attributes and later evolve them into properties with getters and setters without changing the interface of your class, ensuring backward compatibility.

This repository serves as a practical guide for understanding and implementing properties in your Python projects, helping you write more robust, readable, and maintainable object-oriented code.
