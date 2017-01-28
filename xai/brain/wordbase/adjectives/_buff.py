

#calss header
class _BUFF():
	def __init__(self,): 
		self.name = "BUFF"
		self.definitions = [u'(of) a pale, yellowish-brown colour: ', u'If a man is buff, he has a body that is a good shape, and looks as if he has done a lot of exercise: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
