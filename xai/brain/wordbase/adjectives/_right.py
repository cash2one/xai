

#calss header
class _RIGHT():
	def __init__(self,): 
		self.name = "RIGHT"
		self.definitions = [u'correct: ', u'If you are right about something or someone, you are correct in your judgment or statement about it, him, or her: ', u'suitable or correct, or as it should be: ', u'used to refer to a person who is considered to be socially important or a place that such people go to: ', u'in the correct position: ', u'considered fair or morally acceptable by most people: ', u'healthy, or working correctly: ', u'used for emphasizing when something is bad: ', u'on or towards the side of your body that is to the east when you are facing north: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
