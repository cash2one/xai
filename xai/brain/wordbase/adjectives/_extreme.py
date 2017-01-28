

#calss header
class _EXTREME():
	def __init__(self,): 
		self.name = "EXTREME"
		self.definitions = [u'very large in amount or degree: ', u'very severe or bad: ', u'Extreme beliefs and political parties are considered by most people to be unreasonable and unacceptable: ', u'at the furthest point, especially from the centre: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
