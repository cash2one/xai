

#calss header
class _FUTURE():
	def __init__(self,): 
		self.name = "FUTURE"
		self.definitions = [u'happening or existing in the future: ', u'The future form of a verb is used when talking about something that will happen or exist: ', u'used when you tell someone something so that it will be known about and can be used in the future: ', u'in order to be used or looked at some time in the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
