

#calss header
class _APT():
	def __init__(self,): 
		self.name = "APT"
		self.definitions = [u'suitable or right for a particular situation: ', u'to be likely to do something or to often do something: ', u'having a natural ability or skill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
