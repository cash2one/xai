

#calss header
class _LONGITUDINAL():
	def __init__(self,): 
		self.name = "LONGITUDINAL"
		self.definitions = [u'used to refer to lines or distances east or west of an imaginary line between the North Pole and the South Pole : ', u'in the long direction of the body or of any body part: ', u'Longitudinal research is done on people or groups over a long period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
