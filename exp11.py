# Map Coloring CSP
class CSP:
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables  # List of variables (regions)
        self.domains = domains      # Dictionary of domains (possible colors for each region)
        self.neighbors = neighbors  # Dictionary of neighbors for each region
        self.constraints = constraints  # Constraint function

    def is_consistent(self, var, value, assignment):
        """Check if the value assignment is consistent with constraints."""
        for neighbor in self.neighbors[var]:
            if neighbor in assignment and not self.constraints(var, value, neighbor, assignment[neighbor]):
                return False
        return True

    def backtrack(self, assignment):
        """Use backtracking to solve the CSP."""
        # If all variables are assigned, return the assignment
        if len(assignment) == len(self.variables):
            return assignment

        # Select an unassigned variable
        var = [v for v in self.variables if v not in assignment][0]

        # Try each value in the domain of the variable
        for value in self.domains[var]:
            if self.is_consistent(var, value, assignment):
                # Assign the value and proceed with backtracking
                assignment[var] = value
                result = self.backtrack(assignment)
                if result:
                    return result
                assignment.pop(var)

        return None  # Failure

# Constraint function to ensure no adjacent regions have the same color
def map_coloring_constraint(var1, color1, var2, color2):
    return color1 != color2

# Define variables (regions)
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# Define domains (possible colors)
domains = {
    'WA': ['Red', 'Green', 'Blue'],
    'NT': ['Red', 'Green', 'Blue'],
    'SA': ['Red', 'Green', 'Blue'],
    'Q': ['Red', 'Green', 'Blue'],
    'NSW': ['Red', 'Green', 'Blue'],
    'V': ['Red', 'Green', 'Blue'],
    'T': ['Red', 'Green', 'Blue']
}

# Define neighbors (adjacent regions)
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

# Create the CSP instance
csp = CSP(variables, domains, neighbors, map_coloring_constraint)

# Solve the CSP using backtracking
solution = csp.backtrack({})

if solution:
    print("Solution:", solution)
else:
    print("No solution found.")
