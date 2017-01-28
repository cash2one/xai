

#calss header
class _OFF():
	def __init__(self,): 
		self.name = "OFF"
		self.definitions = [u'(of an arranged event) stopped or given up: ', u'having a particular amount or number, especially of money: ', u'below the usual standard or rate: ', u'(of food and drink) no longer fresh or good to eat or drink because of being too old: ', u'(of food in a restaurant) not available at that particular time: ', u"not thinking or worrying about other people's feelings; rude: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
