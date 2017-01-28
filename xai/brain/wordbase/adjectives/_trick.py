

#calss header
class _TRICK():
	def __init__(self,): 
		self.name = "TRICK"
		self.definitions = [u'used to deceive someone, either as a joke or form of entertainment or so that they makes a mistake: ', u'A trick part of the body, especially a joint (= place where two bones are connected), sometimes feels weak suddenly and unexpectedly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
