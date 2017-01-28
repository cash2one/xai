

#calss header
class _INTERESTED():
	def __init__(self,): 
		self.name = "INTERESTED"
		self.definitions = [u'wanting to give your attention to something and discover more about it: ', u'relating to a person or group who has a connection with a particular situation, event, business, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
