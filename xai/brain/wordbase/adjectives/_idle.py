

#calss header
class _IDLE():
	def __init__(self,): 
		self.name = "IDLE"
		self.definitions = [u'not working or being used: ', u'An idle moment or period of time is one in which there is no work or activity: ', u'without work: ', u'without any particular purpose: ', u'lazy and not willing to work: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
