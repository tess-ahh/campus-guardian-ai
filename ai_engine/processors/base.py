class FramePlugin:
    """
    Base interface for all AI plugins.
    """

    def process(self, frame, context=None):
        """
        Process frame and return modified frame.

        Parameters:
        frame: numpy array
        context: shared data between plugins

        Returns:
        frame, context
        """
        return frame, context