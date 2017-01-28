

#calss header
class _SAFE():
	def __init__(self,): 
		self.name = "SAFE"
		self.definitions = [u'not in danger or likely to be harmed: ', u'not harmed or damaged: ', u'completely safe and without injury or damage: ', u'not dangerous or likely to cause harm: ', u'(of a place) where something is not likely to be lost or stolen: ', u'used to refer to things that do not involve any risk: ', u'If an official elected position in is safe, it is likely to be won by the political party that has won it at previous elections: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
