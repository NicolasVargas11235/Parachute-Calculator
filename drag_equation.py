AIR_DENSITY_KPA = 101.325

def drag(drag_coefficient: float, velocity: float, area: float) -> float:
    '''Evaluate drag from the drag eqn.
    '''
    drag = drag_coefficient * AIR_DENSITY_KPA * velocity ** 2 * area / 2
    return drag


print('hi')
