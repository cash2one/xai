

#calss header
class _STRANDED():
	def __init__(self,): 
		self.name = "STRANDED"
		self.definitions = [u'unable to leave somewhere because of a problem such as not having any transport or money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
