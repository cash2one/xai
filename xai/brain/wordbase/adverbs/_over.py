

#calss header
class _OVER():
	def __init__(self,): 
		self.name = "OVER"
		self.definitions = [u'from a higher to a lower position; down: ', u'across; from one side or place to another: ', u'used to describe the way an object moves or is moved so that a different part of it is facing up: ', u'changing or exchanging position: ', u'above or higher than something else, sometimes so that one thing covers the other: ', u'more than a particular amount or level: ', u'(especially of an event) finished: ', u'completely finished: ', u'extra; not used: ', u'again or repeatedly: ', u'said when you are talking to someone by radio, to mean that you have finished speaking and will wait for their answer: ', u'said when you are talking to someone by radio in order to end the conversation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
