

#calss header
class _FRAYED():
	def __init__(self,): 
		self.name = "FRAYED"
		self.definitions = [u'with the threads at the edge coming loose: ', u"used to describe someone's mood when they are feeling worried, upset, or annoyed: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
