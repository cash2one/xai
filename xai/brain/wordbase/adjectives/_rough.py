

#calss header
class _ROUGH():
	def __init__(self,): 
		self.name = "ROUGH"
		self.definitions = [u'not even or smooth, often because of being in bad condition: ', u'If a surface such as paper or skin is rough, it does not feel smooth when you touch it: ', u'Rough ground is ground that is not used for any particular purpose, is not even, and is full of wild plants.', u'not exact or detailed: ', u'used to describe an alcoholic drink, especially wine, that tastes cheap and often strong', u'not made in a careful or expensive way: ', u'A rough voice or sound is hard and loud.', u'If a machine sounds rough, it is making a noise because it is in bad condition.', u'dangerous or violent: ', u'(of the weather or the sea) having strong winds or big waves: ', u'difficult or unpleasant: ', u'ill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
