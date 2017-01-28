

#calss header
class _DIGITAL():
	def __init__(self,): 
		self.name = "DIGITAL"
		self.definitions = [u'recording or storing information as series of the numbers 1 and 0, to show that a signal is present or absent: ', u'using or relating to digital signals and computer technology : ', u'showing information in the form of an electronic image: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
