

#calss header
class _FIT():
	def __init__(self,): 
		self.name = "FIT"
		self.definitions = [u'healthy and strong, especially as a result of exercise: ', u'suitable for a particular purpose or activity: ', u'to not be able to do something because you are upset, ill, drunk, etc.: ', u'safe for people to eat', u'Something that is fit for purpose does what it is meant to do.', u'to consider an action or decision to be correct for the situation: ', u'sexually attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
