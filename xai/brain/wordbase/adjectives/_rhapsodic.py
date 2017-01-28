

#calss header
class _RHAPSODIC():
	def __init__(self,): 
		self.name = "RHAPSODIC"
		self.definitions = [u'in the form of a rhapsody, or expressing powerful feelings: ', u'expressing great enthusiasm about something']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
