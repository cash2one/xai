

#calss header
class _AXIAL():
	def __init__(self,): 
		self.name = "AXIAL"
		self.definitions = [u'relating to or around a real or imaginary straight line going through the centre of an object that is spinning, or a line that divides a symmetrical shape into two equal halves', u'relating to an imaginary line through the centre of the body', u'relating to the axis (= the second of the small bones in the neck that form the spine and support the skull)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
